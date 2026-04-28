import {
  BarChart,
  Bar,
  XAxis,
  YAxis,
  CartesianGrid,
  Tooltip,
  Legend,
  ResponsiveContainer,
} from 'recharts'

const truncate = (str, maxLen = 20) =>
  str.length > maxLen ? str.slice(0, maxLen) + '…' : str

const EVMChart = ({ activities }) => {
  if (!activities || activities.length === 0) {
    return (
      <p style={{ color: '#6b7280', fontStyle: 'italic' }}>
        Agrega actividades para ver la gráfica.
      </p>
    )
  }

  const data = activities.map((a) => ({
    name: truncate(a.name),
    pv: parseFloat(a.evm?.pv ?? 0),
    ev: parseFloat(a.evm?.ev ?? 0),
    ac: parseFloat(a.actual_cost ?? 0),
  }))

  return (
    <ResponsiveContainer width="100%" height={300}>
      <BarChart data={data} margin={{ top: 10, right: 20, left: 0, bottom: 5 }}>
        <CartesianGrid strokeDasharray="3 3" />
        <XAxis dataKey="name" />
        <YAxis />
        <Tooltip />
        <Legend />
        <Bar dataKey="pv" name="PV (Valor Planificado)" fill="#3b82f6" />
        <Bar dataKey="ev" name="EV (Valor Ganado)" fill="#22c55e" />
        <Bar dataKey="ac" name="AC (Costo Real)" fill="#f97316" />
      </BarChart>
    </ResponsiveContainer>
  )
}

export default EVMChart
