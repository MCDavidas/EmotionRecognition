import React, {useCallback, useContext, useRef, useState} from 'react'
import {useHttp} from "../hooks/http.hook";
import {AuthContext} from "../context/AuthContext";
import Webcam from "react-webcam";

export const WebCamera = () => {
    const webcamRef = useRef(null);
    const [imgScreenshotSrc, setImgSrc] = useState(null);
    const [intervalID, setIntervalID] = useState(null);
    const {request} = useHttp()
    const auth = useContext(AuthContext)

    async function sendScreenshot() {
        const tempImgSrc = webcamRef.current.getScreenshot();
        setImgSrc(tempImgSrc);
        const screenshot = await request('/api/screenshot/', 'POST', {type: 'image', image: imgScreenshotSrc}, {
            Authorization: `Bearer ${auth.token}`
        })
    }

    const handleSendScreenshot = useCallback(async () => {
        await sendScreenshot();
    },[webcamRef,imgScreenshotSrc])

    const handleStartRecord = useCallback(async () => {
        setIntervalID(setInterval(sendScreenshot, 1000))

    },[webcamRef,imgScreenshotSrc]);

    const handleStopRecord = useCallback(async () => {
        if (intervalID)
            clearInterval(intervalID);
    },[intervalID])

    const handleDownload = useCallback(() => {
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


    return (
        <>
            <div className="Webcam">
                <div className="camera">
                    <Webcam
                        audio={false}
                        ref={webcamRef}
                        screenshotFormat="image/jpeg"
                    />
                </div>
                <div style={{display: 'flex', flexDirection: 'column', marginLeft: "20px"}}>
                    <button style={{marginBottom: "20px"}}
                            className="ScreenshotButton"
                            onClick={handleSendScreenshot}>
                        Screenshot
                    </button>
                    <button
                        style={{marginBottom: "20px"}}
                        className="StartButton"
                        onClick={handleStartRecord}>
                        Start record
                    </button>
                    <button
                        style={{marginBottom: "20px"}}
                        className="StopButton"
                        onClick={handleStopRecord}>
                        Stop record
                    </button>
                    {
                        imgScreenshotSrc
                        && (<button className="DownloadButton" onClick={handleDownload}>Download</button>)
                    }
                </div>

            </div>
        </>
    );
}
