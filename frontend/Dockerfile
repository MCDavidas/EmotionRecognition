FROM node:14-alpine

RUN mkdir /app
RUN mkdir /app/client

WORKDIR /app/client
COPY client/package*.json ./
RUN npm install

WORKDIR /app
COPY package*.json ./
RUN npm install

COPY . .

EXPOSE 3000

CMD [ "npm", "run", "dev" ]
