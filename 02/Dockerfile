FROM golang:alpine

WORKDIR /

COPY go.mod ./
COPY main.go /

RUN go build -o main

CMD ["/main"]