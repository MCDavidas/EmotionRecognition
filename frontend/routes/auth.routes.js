const {Router} = require('express')
const bcrypt = require('bcryptjs') // хеширование паролей и сравнение
const router = Router()
const config = require('config')
const jwt = require('jsonwebtoken')
const {check, validationResult} = require('express-validator')
const User = require('../models/User')

//api/auth/register
//req-запрос(request) res-ответ(response)
router.post(
    '/register',
    //валидаторы
    [
        check('email', 'Incorrect email').isEmail(),
        check('password', 'Minimum password length 6 characters').isLength({min: 6})
    ],
    async (req, res) => {
        try {

            //обработка ошибок при вводе данных пользователя
            const errors = validationResult(req)
            if (!errors.isEmpty()) {
                return res.status(400).json({
                    errors: errors.array(),
                    message: 'Incorrect data'
                })
            }
            const {email, password} = req.body

            const candidate = await User.findOne({email})

            if (candidate) {
                return res.status(400).json({message: 'This user already exists'})
            }

            const hashedPassword = await bcrypt.hash(password, 12)
            const user = new User({email, password: hashedPassword})

            await user.save()

            res.status(201).json({message: 'User registered'})

        } catch (e) {
            res.status(500).json({message: 'Something went wrong. Please try again'})
        }
    })
//api/auth/login
router.post(
    '/login',
    [
        check('email','Enter correct email').normalizeEmail().isEmail(),
        check('password', 'Enter password').exists()
    ],
    async (req, res) => {
        try {

            //обработка ошибок при вводе данных пользователя
            const errors = validationResult(req)
            if (!errors.isEmpty()) {
                return res.status(400).json({
                    errors: errors.array(),
                    message: 'Incorrect data'
                })
            }
            const {email,password} = req.body

            const user =  await User.findOne({email})
            if(!user){
                return res.status(400).json({message: 'User is not found'})
            }
            const isMarch = await bcrypt.compare(password,user.password)

            if(!isMarch){
                return res.status(400).json({message: 'Try again please'})
            }
            const token =  jwt.sign(
                {userId: user.id},
                config.get('jwtSecret'),
                {expiresIn: '1h'} //время сессии
                )
            res.json({token,userId: user.id})


        } catch (e) {
            res.status(500).json({message: 'Something went wrong. Please try again'})
        }
    })
module.exports = router
