const VARIANTS = {
  primary: {
    backgroundColor: '#3b82f6',
    color: '#fff',
    border: 'none',
  },
  danger: {
    backgroundColor: '#dc2626',
    color: '#fff',
    border: 'none',
  },
  secondary: {
    backgroundColor: '#f3f4f6',
    color: '#374151',
    border: '1px solid #d1d5db',
  },
}

const Button = ({ children, onClick, variant = 'primary', disabled = false, type = 'button' }) => {
  const variantStyle = VARIANTS[variant] || VARIANTS.primary
  return (
    <button
      type={type}
      onClick={onClick}
      disabled={disabled}
      style={{
        ...variantStyle,
        padding: '6px 14px',
        borderRadius: '4px',
        cursor: disabled ? 'not-allowed' : 'pointer',
        fontSize: '0.9rem',
        opacity: disabled ? 0.6 : 1,
      }}
    >
      {children}
    </button>
  )
}

export default Button
