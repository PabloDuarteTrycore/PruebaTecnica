import { useState, useEffect, useCallback } from 'react'
import {
  getProjectById,
  createActivity as apiCreateActivity,
  updateActivity as apiUpdateActivity,
  deleteActivity as apiDeleteActivity,
} from '../api/evmApi'

export const useProject = (projectId) => {
  const [project, setProject] = useState(null)
  const [isLoading, setIsLoading] = useState(false)
  const [error, setError] = useState(null)
  const [isMutating, setIsMutating] = useState(false)

  const refetch = useCallback(async () => {
    setIsLoading(true)
    setError(null)
    try {
      const data = await getProjectById(projectId)
      setProject(data)
    } catch (err) {
      if (err.response) {
        if (err.response.status === 404) {
          setError('Proyecto no encontrado')
        } else {
          setError(err.response.data?.message || 'Error al cargar proyecto')
        }
      } else {
        setError('No se puede conectar con el servidor')
      }
    } finally {
      setIsLoading(false)
    }
  }, [projectId])

  useEffect(() => {
    if (projectId) {
      refetch()
    }
  }, [projectId, refetch])

  const addActivity = async (activityData) => {
    setIsMutating(true)
    try {
      await apiCreateActivity(projectId, activityData)
      await refetch()
    } catch (err) {
      if (err.response) {
        setError(err.response.data?.message || 'Error al crear actividad')
      } else {
        setError('No se puede conectar con el servidor')
      }
    } finally {
      setIsMutating(false)
    }
  }

  const editActivity = async (activityId, fields) => {
    setIsMutating(true)
    try {
      await apiUpdateActivity(activityId, fields)
      await refetch()
    } catch (err) {
      if (err.response) {
        setError(err.response.data?.message || 'Error al editar actividad')
      } else {
        setError('No se puede conectar con el servidor')
      }
    } finally {
      setIsMutating(false)
    }
  }

  const removeActivity = async (activityId) => {
    setIsMutating(true)
    try {
      await apiDeleteActivity(activityId)
      await refetch()
    } catch (err) {
      if (err.response) {
        setError(err.response.data?.message || 'Error al eliminar actividad')
      } else {
        setError('No se puede conectar con el servidor')
      }
    } finally {
      setIsMutating(false)
    }
  }

  return {
    project,
    isLoading,
    error,
    isMutating,
    refetch,
    addActivity,
    editActivity,
    removeActivity,
  }
}
