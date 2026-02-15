# Build stage
FROM node:20-alpine AS build
WORKDIR /app

# Dependency layer caching
COPY package.json package-lock.json ./
RUN npm install

# Application build
COPY . .
RUN npm run build

# Production stage
FROM nginx:stable-alpine

# Deploy static assets
COPY --from=build /app/build /usr/share/nginx/html

EXPOSE 80

# Start server
CMD ["nginx", "-g", "daemon off;"]
