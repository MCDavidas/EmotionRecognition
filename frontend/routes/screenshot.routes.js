const {Router} = require('express')
const auth = require('../middleware/auth.middleware')
const router = Router()

router.post('/', auth, async (req,res) => {
    try{
        const imageObj = req.body
        const {image} = req.body

        if(image){
            console.log("success")
            //console.log(image)
        }
        res.status(201).json({image})
    }catch (e) {
        res.status(500).json({message:'Something want wrong!'})
    }
})

module.exports = router
