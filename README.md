
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
