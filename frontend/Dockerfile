# Use a Node base image
FROM node:12-alpine

# Set the working directory in the container
WORKDIR /app

# Copy package.json and install dependencies
COPY package.json ./
RUN npm install

# Bundle app source
COPY . .

# Expose port 3000 to the outside once the container is running
EXPOSE 3000

# Run the app
CMD ["npm", "start"]
