import StatusBadge from '../ui/StatusBadge'
import Button from '../ui/Button'
import { EVM_STATUS } from '../../constants/evm'

const fmt = (val, decimals = 2) => {
  if (val === null || val === undefined) return 'N/A'
  return parseFloat(val).toFixed(decimals)
}

const coloredValue = (val) => {
  if (val === null || val === undefined) return <span>N/A</span>
  const num = parseFloat(val)
  const color = num < 0 ? '#dc2626' : num > 0 ? '#16a34a' : 'inherit'
  return <span style={{ color }}>{fmt(val)}</span>
}

const rowBackground = (interpretation) => {
  if (interpretation === 'inefficient') return EVM_STATUS.inefficient.background
  if (interpretation === 'efficient') return EVM_STATUS.efficient.background
  return 'transparent'
}

const ActivityTable = ({ activities, onEdit, onDelete }) => {
  if (!activities || activities.length === 0) {
    return (
      <p style={{ color: '#6b7280', fontStyle: 'italic' }}>
        No hay actividades registradas. Agrega la primera actividad.
      </p>
    )
  }

  return (
    <div style={{ overflowX: 'auto' }}>
      <table style={{ width: '100%', borderCollapse: 'collapse', fontSize: '0.875rem' }}>
        <thead>
          <tr style={{ backgroundColor: '#f3f4f6' }}>
            <th style={th}>Nombre</th>
            <th style={th}>BAC</th>
            <th style={th}>Av. Planif.</th>
            <th style={th}>Av. Real</th>
            <th style={th}>AC</th>
            <th style={th}>PV</th>
            <th style={th}>EV</th>
            <th style={th}>CV</th>
            <th style={th}>SV</th>
            <th style={th}>CPI</th>
            <th style={th}>SPI</th>
            <th style={th}>EAC</th>
            <th style={th}>VAC</th>
            <th style={th}>Acciones</th>
          </tr>
        </thead>
        <tbody>
          {activities.map((activity) => (
            <tr
              key={activity.id}
              style={{ backgroundColor: rowBackground(activity.evm?.cpi_interpretation) }}
            >
              <td style={td}>{activity.name}</td>
              <td style={td}>{fmt(activity.bac)}</td>
              <td style={td}>{activity.planned_progress}%</td>
              <td style={td}>{activity.actual_progress}%</td>
              <td style={td}>{fmt(activity.actual_cost)}</td>
              <td style={td}>{fmt(activity.evm?.pv)}</td>
              <td style={td}>{fmt(activity.evm?.ev)}</td>
              <td style={td}>{coloredValue(activity.evm?.cv)}</td>
              <td style={td}>{coloredValue(activity.evm?.sv)}</td>
              <td style={td}>
                <StatusBadge
                  interpretation={activity.evm?.cpi_interpretation}
                  label="CPI"
                  value={fmt(activity.evm?.cpi)}
                />
              </td>
              <td style={td}>
                <StatusBadge
                  interpretation={activity.evm?.spi_interpretation}
                  label="SPI"
                  value={fmt(activity.evm?.spi)}
                />
              </td>
              <td style={td}>{activity.evm?.eac !== null ? fmt(activity.evm?.eac) : 'N/A'}</td>
              <td style={td}>{activity.evm?.vac !== null ? fmt(activity.evm?.vac) : 'N/A'}</td>
              <td style={td}>
                <div style={{ display: 'flex', gap: '0.25rem' }}>
                  <Button variant="secondary" onClick={() => onEdit(activity)}>
                    Editar
                  </Button>
                  <Button
                    variant="danger"
                    onClick={() => {
                      if (window.confirm(`¿Eliminar la actividad "${activity.name}"?`)) {
                        onDelete(activity.id)
                      }
                    }}
                  >
                    Eliminar
                  </Button>
                </div>
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  )
}

const th = {
  padding: '8px 10px',
  textAlign: 'left',
  borderBottom: '2px solid #d1d5db',
  whiteSpace: 'nowrap',
}

const td = {
  padding: '8px 10px',
  borderBottom: '1px solid #e5e7eb',
  whiteSpace: 'nowrap',
}

export default ActivityTable
