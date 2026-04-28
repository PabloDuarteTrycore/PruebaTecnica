import StatusBadge from '../ui/StatusBadge'

const fmt = (val, decimals = 2) => {
  if (val === null || val === undefined) return 'N/A'
  return parseFloat(val).toFixed(decimals)
}

const coloredValue = (val) => {
  if (val === null || val === undefined) return 'N/A'
  const num = parseFloat(val)
  const color = num < 0 ? '#dc2626' : num > 0 ? '#16a34a' : 'inherit'
  return <span style={{ color, fontWeight: '600' }}>{fmt(val)}</span>
}

const KPICard = ({ label, children }) => (
  <div style={{
    border: '1px solid #e5e7eb',
    borderRadius: '8px',
    padding: '1rem',
    minWidth: '120px',
    flex: '1',
    backgroundColor: '#fff',
  }}>
    <div style={{ fontSize: '0.75rem', color: '#6b7280', marginBottom: '4px' }}>{label}</div>
    <div style={{ fontSize: '1.1rem', fontWeight: '600' }}>{children}</div>
  </div>
)

const ConsolidatedKPIs = ({ evm }) => {
  if (!evm || parseFloat(evm.total_bac) === 0) {
    return (
      <p style={{ color: '#6b7280', fontStyle: 'italic' }}>
        Agrega actividades para ver los indicadores del proyecto.
      </p>
    )
  }

  return (
    <div>
      <div style={{ display: 'flex', gap: '0.75rem', flexWrap: 'wrap', marginBottom: '0.75rem' }}>
        <KPICard label="BAC Total">{fmt(evm.total_bac)}</KPICard>
        <KPICard label="PV Total">{fmt(evm.total_pv)}</KPICard>
        <KPICard label="EV Total">{fmt(evm.total_ev)}</KPICard>
        <KPICard label="AC Total">{fmt(evm.total_ac)}</KPICard>
      </div>
      <div style={{ display: 'flex', gap: '0.75rem', flexWrap: 'wrap' }}>
        <KPICard label="CPI">
          <StatusBadge
            interpretation={evm.cpi_interpretation}
            label="CPI"
            value={fmt(evm.cpi)}
          />
        </KPICard>
        <KPICard label="SPI">
          <StatusBadge
            interpretation={evm.spi_interpretation}
            label="SPI"
            value={fmt(evm.spi)}
          />
        </KPICard>
        <KPICard label="CV">{coloredValue(evm.cv)}</KPICard>
        <KPICard label="SV">{coloredValue(evm.sv)}</KPICard>
        <KPICard label="EAC">{fmt(evm.eac)}</KPICard>
        <KPICard label="VAC">{coloredValue(evm.vac)}</KPICard>
      </div>
    </div>
  )
}

export default ConsolidatedKPIs
