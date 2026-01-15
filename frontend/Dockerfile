# ---------------------------
# 1. Builder
# ---------------------------
FROM node:22-alpine AS builder

WORKDIR /app

COPY package*.json ./
RUN npm install

COPY . .
RUN npm run build

# ---------------------------
# 2. Runner
# ---------------------------
FROM node:22-alpine AS runner
WORKDIR /app

COPY --from=builder /app/package*.json ./
COPY --from=builder /app/.next ./.next
COPY --from=builder /app/public ./public
RUN npm install --omit=dev

EXPOSE 3000
CMD ["npm", "start"]

