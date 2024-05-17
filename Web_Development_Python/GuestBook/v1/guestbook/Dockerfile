# This Dockerfile uses a multi-stage build to create a Go application and then deploy it using an Ubuntu image.

# First stage: build the Go application
# Use the official Golang image as the base image for the build stage
FROM golang:1.15 as builder

# Install necessary Go dependencies
RUN go get github.com/codegangsta/negroni
RUN go get github.com/gorilla/mux 
RUN go get github.com/xyproto/simpleredis/v2

# Copy the main Go source file into the container
COPY main.go .

# Build the Go application
RUN go build main.go

# Second stage: create the final image
# Use the official Ubuntu 18.04 image as the base image for the final stage
FROM ubuntu:18.04

# Copy the built Go application from the builder stage to the final image
COPY --from=builder /go//main /app/guestbook

# Add the static website files to the appropriate directory in the final image
ADD public/index.html /app/public/index.html
ADD public/script.js /app/public/script.js
ADD public/style.css /app/public/style.css
ADD public/jquery.min.js /app/public/jquery.min.js

# Set the working directory in the container
WORKDIR /app

# Define the command to run the application
CMD ["./guestbook"]

# Expose port 3000 to allow access to the application
EXPOSE 3000
