import { getEvmStatus } from '../../constants/evm'

const StatusBadge = ({ interpretation, label, value }) => {
  const status = getEvmStatus(interpretation)

  const style = {
    display: 'inline-block',
    padding: '2px 8px',
    borderRadius: '4px',
    fontSize: '0.85rem',
    fontWeight: '600',
    color: status.color,
    backgroundColor: status.background,
    border: `1px solid ${status.color}`,
  }

  if (label && value !== undefined) {
    return <span style={style}>{`${label}: ${value}`}</span>
  }

  return <span style={style}>{status.text}</span>
}

export default StatusBadge
