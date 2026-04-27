const spinnerStyle = {
  display: 'flex',
  justifyContent: 'center',
  alignItems: 'center',
  padding: '2rem',
  fontSize: '1rem',
  color: '#6b7280',
}

const LoadingSpinner = () => {
  return (
    <div style={spinnerStyle}>
      <span>Cargando...</span>
    </div>
  )
}

export default LoadingSpinner
