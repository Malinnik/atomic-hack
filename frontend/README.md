# Frontend

## Описание
Это проект, написанный на [Next.js](https://nextjs.org/). Предоставляет небольшой интерфейс для взаимойдействия с сервером и отправки фотографий сварочных швов на проверку

## Быстрый старт

`docker run -d -p 3000:3000 horaziy/atomic-hack-frontend`

## Сборка приложения
Загрузите приложение
```bash
git clone https://github.com/Malinnik/atomic-hack.git
cd atomic-hack/frontend
```
Используйте Docker для сборки проекта
`docker build -t atomic-hack-frontend:latest .`

## Редактирование приложения
Используйте команды для запуска приложения в формате разработки
```bash
npm run dev
# or
yarn dev
# or
pnpm dev
# or
bun dev
```
Откройте [http://localhost:3000](http://localhost:3000) в браузере, чтобы увидеть результат


