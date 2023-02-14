import React from 'react'
import ReactDOM from 'react-dom/client'
import { BrowserRouter, Routes, Route } from 'react-router-dom'
import './index.css'
import PatternCreate from './views/PatternCreate'
import ZenbedController from './views/ZenbedController'

const root = ReactDOM.createRoot(document.getElementById('root'))
root.render(
  <BrowserRouter>
    <Routes>
      <Route path='/' element={<ZenbedController />} />
      <Route path='/create' element={<PatternCreate />} />
    </Routes>
  </BrowserRouter>
)
