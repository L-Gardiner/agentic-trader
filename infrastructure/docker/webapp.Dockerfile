FROM node:18-alpine as builder

WORKDIR /app

# Copy package files
COPY frontend-webapp/package*.json ./

# Install dependencies
RUN npm ci

# Copy application code
COPY frontend-webapp/ ./

# Build the application
RUN npm run build

# Production stage
FROM nginx:alpine

# Copy built assets from builder stage
COPY --from=builder /app/build /usr/share/nginx/html

# Copy nginx configuration
COPY infrastructure/docker/nginx.conf /etc/nginx/conf.d/default.conf

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
