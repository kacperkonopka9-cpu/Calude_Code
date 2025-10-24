/**
 * Application configuration
 * Never access import.meta.env directly - always use this config object
 */
export const config = {
  apiBaseUrl: import.meta.env.VITE_API_BASE_URL || 'http://localhost:8000/v1',
  wsUrl: import.meta.env.VITE_WS_URL || 'ws://localhost:8000/ws',
  cognito: {
    userPoolId: import.meta.env.VITE_COGNITO_USER_POOL_ID || '',
    clientId: import.meta.env.VITE_COGNITO_CLIENT_ID || '',
  },
  awsRegion: import.meta.env.VITE_AWS_REGION || 'eu-central-1',
} as const;
