import { useState } from 'react'
import { useParams, useNavigate } from 'react-router-dom'
import { useProject } from '../hooks/useProject'
import ConsolidatedKPIs from '../components/evm/ConsolidatedKPIs'
import EVMChart from '../components/evm/EVMChart'
import ActivityTable from '../components/evm/ActivityTable'
import ActivityForm from '../components/evm/ActivityForm'
import LoadingSpinner from '../components/ui/LoadingSpinner'
import Button from '../components/ui/Button'

const ProjectDetailPage = () => {
  const { projectId } = useParams()
  const navigate = useNavigate()
  const { project, isLoading, error, isMutating, addActivity, editActivity, removeActivity } =
    useProject(projectId)

  const [showForm, setShowForm] = useState(false)
  const [editingActivity, setEditingActivity] = useState(null)

  if (isLoading && !project) return <LoadingSpinner />
  if (error) return <p style={{ color: '#dc2626' }}>Error: {error}</p>
  if (!project) return null

  const handleAddSubmit = async (data) => {
    await addActivity(data)
    setShowForm(false)
  }

  const handleEditSubmit = async (data) => {
    await editActivity(editingActivity.id, data)
    setEditingActivity(null)
    setShowForm(false)
  }

  const handleEditClick = (activity) => {
    setEditingActivity(activity)
    setShowForm(true)
  }

  const handleCancel = () => {
    setShowForm(false)
    setEditingActivity(null)
  }

  const handleAddClick = () => {
    setEditingActivity(null)
    setShowForm(true)
  }

  return (
    <div style={{ maxWidth: '1200px', margin: '0 auto', padding: '1.5rem' }}>
      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'flex-start', marginBottom: '1rem' }}>
        <div>
          <h1 style={{ margin: 0 }}>{project.name}</h1>
          {project.description && (
            <p style={{ color: '#6b7280', margin: '4px 0 0' }}>{project.description}</p>
          )}
        </div>
        <Button variant="secondary" onClick={() => navigate('/')}>
          ← Volver a lista
        </Button>
      </div>

      <section style={{ marginBottom: '1.5rem' }}>
        <h2 style={{ marginBottom: '0.75rem' }}>KPIs del Proyecto</h2>
        <ConsolidatedKPIs evm={project.evm} />
      </section>

      <section style={{ marginBottom: '1.5rem' }}>
        <h2 style={{ marginBottom: '0.75rem' }}>PV vs EV vs AC por Actividad</h2>
        <EVMChart activities={project.activities} />
      </section>

      <section>
        <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '0.75rem' }}>
          <h2 style={{ margin: 0 }}>Actividades</h2>
          {!showForm && (
            <Button onClick={handleAddClick}>+ Agregar actividad</Button>
          )}
        </div>

        {showForm && (
          <ActivityForm
            onSubmit={editingActivity ? handleEditSubmit : handleAddSubmit}
            onCancel={handleCancel}
            initialValues={editingActivity}
            isLoading={isMutating}
          />
        )}

        <ActivityTable
          activities={project.activities}
          onEdit={handleEditClick}
          onDelete={removeActivity}
        />
      </section>
    </div>
  )
}

export default ProjectDetailPage
