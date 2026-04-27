export const EVM_STATUS = {
  efficient: {
    color: '#16a34a',
    background: '#dcfce7',
    text: 'Eficiente',
  },
  on_track: {
    color: '#ca8a04',
    background: '#fef9c3',
    text: 'En línea',
  },
  inefficient: {
    color: '#dc2626',
    background: '#fee2e2',
    text: 'Ineficiente',
  },
  insufficient_data: {
    color: '#6b7280',
    background: '#f3f4f6',
    text: 'Sin datos',
  },
}

export const getEvmStatus = (interpretation) =>
  EVM_STATUS[interpretation] || EVM_STATUS.insufficient_data
