FROM node:20-alpine

WORKDIR /app
COPY server.js .

RUN npm install express redis

EXPOSE 80
CMD ["node", "server.js"]
