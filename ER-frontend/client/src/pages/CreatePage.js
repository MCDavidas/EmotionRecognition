import React, {useContext, useEffect, useState} from 'react'
<<<<<<< HEAD
import {useHttp} from '../hooks/http.hook'
import {AuthContext} from '../context/AuthContext'
import {useHistory} from 'react-router-dom'

export const CreatePage = () => {
    const history = useHistory()
    const auth = useContext(AuthContext)
    const {request} = useHttp()
    const [link, setLink] = useState('')

    useEffect(() => {
        window.M.updateTextFields()
    }, [])

    const pressHandler = async event => {
        if (event.key === 'Enter') {
            try {
                const data = await request('/api/link/generate', 'POST', {from: link}, {
                    Authorization: `Bearer ${auth.token}`
                })
                history.push(`/detail/${data.link._id}`)
            } catch (e) {}
        }
    }

=======
import {useHttp} from "../hooks/http.hook";
import {AuthContext} from "../context/AuthContext";
import {useHistory} from 'react-router-dom'

export const CreatePage = () => {
    const auth = useContext(AuthContext)
    const history = useHistory()
    const {request} = useHttp()
    const [link, setLink] = useState('')
    useEffect(()=>{
        window.M.updateTextFields()},[])
    const pressHandler = async event => {

        if (event.key === 'Enter') {
            try {
                const data = await request('/api/link/generate', 'POST', {from: link},{
                    Authorization: `Bearer' ${auth.token}`
                })

                history.push(`/detail/${data.link._id}`)

                console.log(data)
            } catch (e) {

            }
        }

    }
>>>>>>> liubov-frontend
    return (
        <div className="row">
            <div className="col s8 offset-s2" style={{paddingTop: '2rem'}}>
                <div className="input-field">
                    <input
<<<<<<< HEAD
                        placeholder="Вставьте ссылку"
=======
                        placeholder="Insert link"
>>>>>>> liubov-frontend
                        id="link"
                        type="text"
                        value={link}
                        onChange={e => setLink(e.target.value)}
                        onKeyPress={pressHandler}
                    />
<<<<<<< HEAD
                    <label htmlFor="link">Введите ссылку</label>
=======
                    <label htmlFor="link">Enter link</label>
>>>>>>> liubov-frontend
                </div>
            </div>
        </div>
    )
}
