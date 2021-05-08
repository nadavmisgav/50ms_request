FROM alpine
RUN apk add strace ltrace nodejs npm
RUN npm install express --save
RUN mkdir /public
COPY server.js .
CMD [ "node", "server.js" ]