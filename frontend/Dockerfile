# Use Node 22 (recommended for Next.js 16+)
FROM node:22-alpine AS builder

WORKDIR /app

# Install dependencies
COPY package*.json ./
RUN npm install

# Copy source code
COPY . .

# Build Next.js
RUN npm run build

# Production image
FROM node:22-alpine AS runner

WORKDIR /app

COPY --from=builder /app/.next .next
COPY --from=builder /app/public public
COPY package*.json ./

# Install only production deps
RUN npm install --omit=dev

EXPOSE 3000

CMD ["npm", "start"]

