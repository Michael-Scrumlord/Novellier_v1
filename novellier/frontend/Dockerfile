# Node base image
FROM node:16-alpine

# Set working directory
WORKDIR /app

# Copy package.json and package-lock.json (if available)
COPY package.json ./
COPY package-lock.json ./
# If you have a yarn.lock file, you would copy that instead for yarn

# Install dependencies
RUN npm install

# Copy application code
COPY . .

# Expose port for React app (default is 3000)
EXPOSE 3000

# Command to start the React development server
CMD ["npm", "start"]
