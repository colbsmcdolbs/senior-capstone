FROM node:14.15.4-alpine3.12

RUN mkdir -p /app

WORKDIR /app

COPY package*.json /app/

RUN npm install

COPY . /app/

EXPOSE 4200

CMD ["npm", "start"]
