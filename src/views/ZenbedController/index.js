import react, { useState, useEffect } from 'react'
import axios from 'axios'
import './index.css'

const ZenbedController = () => {
  const [patterns, setPatterns] = useState()

  const playPattern = pattern => {
    axios.post(process.env.REACT_APP_API_ADDRESS + '/zenbed/start_pattern', {
      sequence: pattern.sequence,
    })
  }

  const stopPattern = () => {
    axios.post(process.env.REACT_APP_API_ADDRESS + '/zenbed/stop_pattern')
  }

  const getZenbedPatterns = () => {
    axios.get(process.env.REACT_APP_API_ADDRESS_CREATE + '/api/patterns').then(request => setPatterns(request.data))
  }

  useEffect(() => {
    getZenbedPatterns()
  }, [])

  return (
    <div className='controller-page'>
      <div className='pattern-selection'>
        {patterns &&
          patterns.map(pattern => {
            return (
              <button className='pattern-entry' onClick={() => playPattern(pattern)}>
                Play {pattern.name}
              </button>
            )
          })}
      </div>
      <button
        className='controller-button'
        onClick={() => {
          stopPattern()
        }}
      >
        Stop Pattern
      </button>
    </div>
  )
}

export default ZenbedController
