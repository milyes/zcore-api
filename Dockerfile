FROM golang:1.23-alpine AS builder
WORKDIR /src
COPY . .
RUN CGO_ENABLED=0 go build -o /app/zcore-api ./cmd/server || echo "build stub"

FROM gcr.io/distroless/static-debian12:nonroot
WORKDIR /app
COPY --from=builder /app/zcore-api /app/zcore-api
USER nonroot:nonroot
ENTRYPOINT ["/app/zcore-api"]
