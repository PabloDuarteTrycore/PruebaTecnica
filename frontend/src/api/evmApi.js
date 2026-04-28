import axios from 'axios'

const API_BASE_URL = import.meta.env.VITE_API_URL || 'http://localhost:5000/api/v1'

const axiosInstance = axios.create({
  baseURL: API_BASE_URL,
  timeout: 10000,
  headers: { 'Content-Type': 'application/json' },
})

// --- Proyectos ---

export const getAllProjects = () =>
  axiosInstance.get('/projects/').then((r) => r.data)

export const getProjectById = (projectId) =>
  axiosInstance.get(`/projects/${projectId}`).then((r) => r.data)

export const createProject = (data) =>
  axiosInstance.post('/projects/', data).then((r) => r.data)

export const updateProject = (projectId, data) =>
  axiosInstance.put(`/projects/${projectId}`, data).then((r) => r.data)

export const deleteProject = (projectId) =>
  axiosInstance.delete(`/projects/${projectId}`).then((r) => r.data)

// --- Actividades ---

export const getActivitiesByProject = (projectId) =>
  axiosInstance.get(`/projects/${projectId}/activities`).then((r) => r.data)

export const createActivity = (projectId, data) =>
  axiosInstance
    .post(`/projects/${projectId}/activities`, data)
    .then((r) => r.data)

export const updateActivity = (activityId, data) =>
  axiosInstance.put(`/activities/${activityId}`, data).then((r) => r.data)

export const deleteActivity = (activityId) =>
  axiosInstance.delete(`/activities/${activityId}`).then((r) => r.data)
