
# Start project
from root directoty
`npm run dev`

# Connect with backend
In [`client/src/components/WebCamera.js`](https://github.com/QwaYCh/ERProject/blob/liubov-frontend/ER-frontend/client/src/components/WebCamera.js) method `sendScreenshot()` 1st arg is your `url`
``` javascript
const screenshot = await request(url, 'POST', {type: 'image', image: imgScreenshotSrc}, {
                Authorization: `Bearer ${auth.token}`
            })
```

Or create new varible in [`config/default.json`](https://github.com/QwaYCh/ERProject/blob/liubov-frontend/ER-frontend/config/default.json)

# Python server
Скачать anaconda по ссылке внизу страницы: https://www.anaconda.com/products/individual
Вот как создать окружение с помощью environment.yaml: https://stackoverflow.com/questions/48016351/how-to-make-new-anaconda-env-from-yml-file
Активировать окружение с помощью команды `conda activate ERProject`
Для запуска сервера из папки `backend/` выполнить `python run.py server`
