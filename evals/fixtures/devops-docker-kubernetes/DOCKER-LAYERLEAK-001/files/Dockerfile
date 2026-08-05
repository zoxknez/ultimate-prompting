FROM node:22-slim

WORKDIR /app

# Vulnerable: copies the entire build context, including .env (with real
# database and third-party API credentials for local/staging) and the
# deploy/ directory (with an SSH private key used for release pushes), into
# an image layer. No .dockerignore exists in this repository to exclude
# them. Anyone who can pull the built image - including from a registry
# with read access broader than the deploy pipeline - can extract both
# secrets from the image layers even after a later layer deletes the files,
# since deleted files remain recoverable from earlier layers.
COPY . .

RUN npm ci --omit=dev

CMD ["node", "server.js"]
