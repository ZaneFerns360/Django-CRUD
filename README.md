# django-tailwinds
starter config for django + tailwinds + flowbite

## Make Database Migrations:
```bash
python manage.py migrate 
# &
python manage.py makemigrations business
```
## Install node pakages:
```bash
npm install
# or
yarn install
# or
pnpm install
```
## Start Tailwinds static output (Automatic):
- check the node js pakage manager in manage.py (default = pnpm)
- if your are using npm then replace 'pnpm' with 'npx'
- if your are using yarn then replace 'pnpm' with 'yarn'
- proceed to run server as normal
## Start Tailwinds static output (Manual):
```bash
npx tailwindcss -i ./static/src/input.css -o ./static/src/output.css --watch
# or
yarn tailwindcss -i ./static/src/input.css -o ./static/src/output.css --watch
# or
pnpm tailwindcss -i ./static/src/input.css -o ./static/src/output.css --watch
```
## Run server:
```bash
python manage.py runserver      
```
