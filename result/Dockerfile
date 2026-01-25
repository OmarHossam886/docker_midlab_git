FROM node:20-alpine

WORKDIR /app
COPY server.js .

RUN npm install express redis

CMD ["node", "server.js"]
