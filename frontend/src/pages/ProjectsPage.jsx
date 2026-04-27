import { useState } from 'react'
import { useNavigate } from 'react-router-dom'
import { useProjects } from '../hooks/useProjects'
import LoadingSpinner from '../components/ui/LoadingSpinner'
import Button from '../components/ui/Button'
import StatusBadge from '../components/ui/StatusBadge'

const ProjectsPage = () => {
  const navigate = useNavigate()
  const { projects, isLoading, error, createProject } = useProjects()

  const [showForm, setShowForm] = useState(false)
  const [name, setName] = useState('')
  const [description, setDescription] = useState('')
  const [formError, setFormError] = useState('')

  const handleCreate = async (e) => {
    e.preventDefault()
    if (!name.trim()) {
      setFormError('El nombre del proyecto es requerido')
      return
    }
    setFormError('')
    await createProject(name.trim(), description.trim())
    setName('')
    setDescription('')
    setShowForm(false)
  }

  return (
    <div style={{ maxWidth: '900px', margin: '0 auto', padding: '1.5rem' }}>
      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '1rem' }}>
        <h1 style={{ margin: 0 }}>Proyectos</h1>
        {!showForm && (
          <Button onClick={() => setShowForm(true)}>+ Nuevo proyecto</Button>
        )}
      </div>

      {showForm && (
        <form
          onSubmit={handleCreate}
          style={{ border: '1px solid #e5e7eb', borderRadius: '6px', padding: '1rem', marginBottom: '1.5rem' }}
        >
          <h3 style={{ marginTop: 0 }}>Nuevo proyecto</h3>
          <div style={{ marginBottom: '0.75rem' }}>
            <label>Nombre del proyecto</label>
            <input
              value={name}
              onChange={(e) => setName(e.target.value)}
              style={{ display: 'block', width: '100%', marginTop: '4px', padding: '6px', boxSizing: 'border-box' }}
            />
            {formError && <span style={{ color: '#dc2626', fontSize: '0.8rem' }}>{formError}</span>}
          </div>
          <div style={{ marginBottom: '1rem' }}>
            <label>Descripción (opcional)</label>
            <textarea
              value={description}
              onChange={(e) => setDescription(e.target.value)}
              rows={3}
              style={{ display: 'block', width: '100%', marginTop: '4px', padding: '6px', boxSizing: 'border-box' }}
            />
          </div>
          <div style={{ display: 'flex', gap: '0.5rem' }}>
            <Button type="submit" disabled={isLoading}>Crear</Button>
            <Button variant="secondary" onClick={() => setShowForm(false)}>Cancelar</Button>
          </div>
        </form>
      )}

      {error && <p style={{ color: '#dc2626' }}>Error: {error}</p>}

      {isLoading && projects.length === 0 ? (
        <LoadingSpinner />
      ) : projects.length === 0 ? (
        <p style={{ color: '#6b7280', fontStyle: 'italic' }}>No hay proyectos. Crea el primero.</p>
      ) : (
        <table style={{ width: '100%', borderCollapse: 'collapse', fontSize: '0.9rem' }}>
          <thead>
            <tr style={{ backgroundColor: '#f3f4f6' }}>
              <th style={th}>Nombre</th>
              <th style={th}>Descripción</th>
              <th style={th}>CPI</th>
              <th style={th}>SPI</th>
              <th style={th}></th>
            </tr>
          </thead>
          <tbody>
            {projects.map((p) => (
              <tr key={p.id} style={{ borderBottom: '1px solid #e5e7eb' }}>
                <td style={td}>{p.name}</td>
                <td style={td}>{p.description || '—'}</td>
                <td style={td}>
                  <StatusBadge
                    interpretation={p.evm?.cpi_interpretation}
                    label="CPI"
                    value={p.evm?.cpi ? parseFloat(p.evm.cpi).toFixed(2) : null}
                  />
                </td>
                <td style={td}>
                  <StatusBadge
                    interpretation={p.evm?.spi_interpretation}
                    label="SPI"
                    value={p.evm?.spi ? parseFloat(p.evm.spi).toFixed(2) : null}
                  />
                </td>
                <td style={td}>
                  <Button onClick={() => navigate(`/projects/${p.id}`)}>Ver detalle</Button>
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      )}
    </div>
  )
}

const th = { padding: '8px 10px', textAlign: 'left', borderBottom: '2px solid #d1d5db' }
const td = { padding: '8px 10px' }

export default ProjectsPage
