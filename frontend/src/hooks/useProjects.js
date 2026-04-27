import { useState, useEffect, useCallback } from 'react'
import { getAllProjects, createProject as apiCreateProject } from '../api/evmApi'

export const useProjects = () => {
  const [projects, setProjects] = useState([])
  const [isLoading, setIsLoading] = useState(false)
  const [error, setError] = useState(null)

  const fetchProjects = useCallback(async () => {
    setIsLoading(true)
    setError(null)
    try {
      const data = await getAllProjects()
      setProjects(data)
    } catch (err) {
      if (err.response) {
        setError(err.response.data?.message || 'Error al cargar proyectos')
      } else {
        setError('No se puede conectar con el servidor')
      }
    } finally {
      setIsLoading(false)
    }
  }, [])

  useEffect(() => {
    fetchProjects()
  }, [fetchProjects])

  const createProject = async (name, description) => {
    setIsLoading(true)
    setError(null)
    try {
      await apiCreateProject({ name, description })
      await fetchProjects()
    } catch (err) {
      if (err.response) {
        setError(err.response.data?.message || 'Error al crear proyecto')
      } else {
        setError('No se puede conectar con el servidor')
      }
    } finally {
      setIsLoading(false)
    }
  }

  return {
    projects,
    isLoading,
    error,
    fetchProjects,
    createProject,
  }
}
