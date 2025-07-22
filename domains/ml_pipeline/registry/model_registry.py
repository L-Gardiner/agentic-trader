from typing import Dict, Any, List, Optional
from datetime import datetime
import mlflow
from mlflow.tracking import MlflowClient
from pathlib import Path

class ModelRegistry:
    """Manages model versioning and deployment."""
    
    def __init__(self, tracking_uri: str, registry_uri: str):
        mlflow.set_tracking_uri(tracking_uri)
        self.client = MlflowClient(registry_uri=registry_uri)

    async def register_model(
        self,
        model_uri: str,
        name: str,
        version: Optional[str] = None,
        metadata: Optional[Dict[str, Any]] = None
    ) -> str:
        """Register a model in the registry."""
        try:
            result = mlflow.register_model(
                model_uri=model_uri,
                name=name
            )
            
            if metadata:
                self.client.set_model_version_tag(
                    name=name,
                    version=result.version,
                    key="metadata",
                    value=str(metadata)
                )
            
            return result.version
        except Exception as e:
            raise RuntimeError(f"Failed to register model: {str(e)}")

    async def load_model(
        self,
        name: str,
        version: Optional[str] = None,
        stage: Optional[str] = None
    ) -> Any:
        """Load a model from the registry."""
        if version:
            model_uri = f"models:/{name}/{version}"
        elif stage:
            model_uri = f"models:/{name}/{stage}"
        else:
            model_uri = f"models:/{name}/latest"
            
        return mlflow.pyfunc.load_model(model_uri)

    async def promote_model(
        self,
        name: str,
        version: str,
        stage: str
    ) -> bool:
        """Promote a model to a new stage (staging/production)."""
        try:
            self.client.transition_model_version_stage(
                name=name,
                version=version,
                stage=stage
            )
            return True
        except Exception as e:
            raise RuntimeError(f"Failed to promote model: {str(e)}")

    async def get_model_metadata(
        self,
        name: str,
        version: Optional[str] = None
    ) -> Dict[str, Any]:
        """Get model metadata from the registry."""
        try:
            if version:
                model_version = self.client.get_model_version(name, version)
            else:
                model_version = self.client.get_latest_versions(name)[0]
            
            return {
                "name": name,
                "version": model_version.version,
                "stage": model_version.current_stage,
                "creation_timestamp": model_version.creation_timestamp,
                "last_updated_timestamp": model_version.last_updated_timestamp,
                "description": model_version.description,
                "tags": model_version.tags
            }
        except Exception as e:
            raise RuntimeError(f"Failed to get model metadata: {str(e)}")
