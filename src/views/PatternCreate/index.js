import react, { useState, useEffect } from 'react'
import axios from 'axios'
import './index.css'

// list of colors
const colors = [
  'rgb(255,0,0)', // red
  'rgb(255,153,0)', // orange
  'rgb(255,255,0)', // yellow
  'rgb(0,255,0)', // green
  'rgb(0,255,255)', // blue
  'rgb(0,0,255)', // dark blue
  'rgb(75,0,130)', // purple
  'rgb(148,0,211)', // dark purple
]

const colors_faded = [
  'rgb(234, 153, 153)', // red faded
  'rgb(249, 203, 156)', // orange faded
  'rgb(255, 229, 153)', // yellow faded
  'rgb(182, 215, 168)', // green faded
  'rgb(162, 196, 201)', // blue faded
  'rgb(159, 197, 232)', // dark blue faded
  'rgb(180, 167, 214)', // dark purple faded
  'rgb(213, 166, 189)', // purple faded
]

const PatternCreate = () => {
  const [zenbedGrid, setZenbedGrid] = useState()
  const cellClicked = cell => {
    console.log((cell.target.style.backgroundColor = 'red'))
  }

  const zenbedOn = () => {
    axios.post(process.env.REACT_APP_API_ADDRESS + '/zenbed/start_pattern')
  }

  const zenbedOff = () => {
    axios.post(process.env.REACT_APP_API_ADDRESS + '/zenbed/stop_pattern')
  }

  return (
    <div className='pattern-create-page'>
      <h1>Pattern Creation</h1>

      <div id='grid' className='col-lg-6' align='center'>
        <h2 className='text-center'>Zenbed</h2>

        <div id='zenbed' className='grid-container' data-toggle='collapse'>
          <div id='grid-item-border'></div>
          <div id='grid-item-border'>A1 </div>
          <div id='grid-item-border'>B1 </div>
          <div id='grid-item-border'>C1 </div>
          <div id='grid-item-border'>D1 </div>
          <div id='grid-item-border'>E1 </div>
          <div id='grid-item-border'>F1 </div>
          <div id='grid-item-border'>G1 </div>
          <div id='grid-item-border'>H1 </div>
          <div id='grid-item-border'>I1 </div>
          <div id='grid-item-border'>J1 </div>
          <div id='grid-item-border'>K1 </div>
          <div id='grid-item-border'>L1 </div>
          <div id='grid-item-border'>A1 </div>

          {[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18].map(number => {
            {
              return (
                <>
                  <div id='grid-item-border'>{number}</div>
                  {['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L'].map(letter => {
                    return (
                      <>
                        <div
                          onClick={cell => {
                            cellClicked(cell)
                          }}
                          className='grid-item'
                        >
                          {number}
                          {letter}
                        </div>
                      </>
                    )
                  })}
                  <div id='grid-item-border'>{number}</div>
                </>
              )
            }
          })}

          <div id='grid-item-border'></div>
          <div id='grid-item-border'>A</div>
          <div id='grid-item-border'>B</div>
          <div id='grid-item-border'>C</div>
          <div id='grid-item-border'>D</div>
          <div id='grid-item-border'>E</div>
          <div id='grid-item-border'>F</div>
          <div id='grid-item-border'>G</div>
          <div id='grid-item-border'>H</div>
          <div id='grid-item-border'>I</div>
          <div id='grid-item-border'>J</div>
          <div id='grid-item-border'>K</div>
          <div id='grid-item-border'>L</div>
          <div id='grid-item-border'></div>
        </div>
      </div>
      <button onClick={() => zenbedOn()}>Play Pattern</button>
      <button onClick={() => zenbedOn()}>Stop Pattern</button>
    </div>
  )
}

export default PatternCreate
