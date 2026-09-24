#!/bin/sh
set -eu
# Credentials remain environment references; do not enable shell tracing.
: "${NEXT_PUBLIC_WEBAPP_URL:?Set the public HTTPS origin}"
: "${DATABASE_URL:?Set the database connection binding}"
: "${DATABASE_DIRECT_URL:?Set the direct database connection binding}"
: "${NEXTAUTH_SECRET:?Set the session secret}"
: "${CALENDSO_ENCRYPTION_KEY:?Set the encryption key}"
scripts/replace-placeholder.sh "$BUILT_NEXT_PUBLIC_WEBAPP_URL" "$NEXT_PUBLIC_WEBAPP_URL"
./node_modules/.bin/prisma migrate deploy --schema /calcom/packages/prisma/schema.prisma
./node_modules/.bin/ts-node --transpile-only /calcom/scripts/seed-app-store.ts
exec yarn start
