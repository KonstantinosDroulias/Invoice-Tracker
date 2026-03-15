#!/bin/bash
set -e

# Install npm deps if needed
if [ -f package.json ]; then
  npm install
fi

# Build Tailwind CSS (v4 CLI)
npm run build

# Collect Django static files
python manage.py collectstatic --noinput
