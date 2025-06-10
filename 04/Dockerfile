FROM golang:1.23.5-alpine3.21 AS builder
#コンテナに移動するためのコマンド
WORKDIR /
COPY main.go .
RUN go build -o main main.go


FROM alpine:latest
WORKDIR /app

COPY --from=builder /main .

CMD ["./main"]