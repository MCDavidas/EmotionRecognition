import React from 'react'

export const ImageInput = () => {
    
    const [imgInputSrc, setImgInputSrc] = React.useState(null);

    const handleDisplay = React.useCallback((e) => {
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
    }, [imgInputSrc])

    const handleClear = React.useCallback(() => {
        setImgInputSrc("")

    }, [imgInputSrc]);
    return (
        <>
            <div className="FileInput">
                <input
                    className="fileInput"
                    id="fileInput"
                    type="file"
                    onChange={handleDisplay}
                />
                <label
                    className="ImageInputButton"
                    htmlFor="fileInput">
                    Image input
                </label>
                <img
                    className="inputImage"
                    src={imgInputSrc}
                    height="500"
                    alt=""
                />
                {
                    imgInputSrc
                    && (<button className="ClearButton" onClick={handleClear}>Clear</button>)
                }
            </div>
        </>
    )
}
