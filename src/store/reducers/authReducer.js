const initState = {
  authError: null
}

const authReducer = (state = initState, action) => {
  switch(action.type) {
    case 'SIGNUP_ERROR':
      console.log('signup error', action.err);
      return {
        ...state,
        authError: 'Signup failed'
      }
    case 'SIGNUP_SUCCESS':
      return {
        ...state,
        authError: null
      }
    case 'VERIF_ERROR':
      return {
        ...state,
        authError: 'Missing email or password or passwords do not match'
      }
    case 'LOGIN_ERROR':
      console.log('login error', action.err);
      return {
        ...state,
        authError: 'Login failed'
      }
    case 'LOGIN_SUCCESS':
      console.log('login success');
      return {
        ...state,
        authError: null
      }
    case 'SIGNOUT_SUCCESS':
      console.log('signout success');
      return state
    default:
      return state
  }
};

export default authReducer;