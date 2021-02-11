import React, {useContext} from 'react'
import '../public/stylesheets/camera-page.css'
import {WebCamera} from "../components/WebCamera";
import {ImageInput} from "../components/ImageInput";

export const CameraPage = () => {

/*
    var websocket = new WebSocket("ws://localhost:56789/");
    const webcamRef = React.useRef(null);
    const [imgScreenshotSrc, setImgSrc] = React.useState(null);
    const [imgInputSrc, setImgInputSrc] = React.useState(null);
    //const inputFile = React.createRef();

    websocket.onmessage = function (event) {
        var data = JSON.parse(event.data);
        switch (data.type) {
            case 'image':
                setImgSrc('data:image/jpeg;base64,' + data.image);
                break;
            default:
                break;
        }
    };

    const capture = React.useCallback(() => {
        //скрин с камеры (его можно скачать)
        const tempImgSrc = webcamRef.current.getScreenshot();
        setImgSrc(tempImgSrc);

        websocket.send(JSON.stringify({type: 'image', image: tempImgSrc}));
    }, [webcamRef, setImgSrc]);

    const handleDownload = React.useCallback(() => {
        if (imgScreenshotSrc) {
            const link = document.createElement("a");
            document.body.appendChild(link);
            link.href = imgScreenshotSrc;
            let data = new Date();
            const imageName = `${data.getDate()}${data.getMonth()}${data.getFullYear()}_${data.getHours()}${data.getMinutes()}${data.getSeconds()}_${data.getMilliseconds()}`
            link.download = `${imageName}.jpeg`;
            link.click();
            window.URL.revokeObjectURL(imgScreenshotSrc);

        }
    }, [imgScreenshotSrc]);

    const handleSend = React.useCallback(() => {
    }, []);

    const handleClear = React.useCallback(() => {
        setImgInputSrc("")

    }, [setImgInputSrc]);

    const handleDisplay = e => {
        //изображение из файловой системы

        // let file = inputFile.current.files[0];
        let file = e.target.files[0];
        let reader = new FileReader();
        reader.onloadend = () => {
            setImgInputSrc(reader.result)
        }
        if (file) {
            reader.readAsDataURL(file);
        } else {
            setImgInputSrc("");
        }


    }
*/

    return (
        <>
            <h2>Image from camera</h2>
            <WebCamera/>
            <h2>Image from file system</h2>
            <ImageInput/>
        </>
    );

}
