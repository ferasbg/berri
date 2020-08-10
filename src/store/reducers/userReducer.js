const initState = {};

const userReducer = (state = initState, action) => {
  switch (action.type) {
    case 'CREATE_USER':
      console.log('create user', action.user);
      return state;
    case 'CREATE_USER_ERROR':
      console.log('create user error', action.err);
      return state;
    default:
      return state;
  }
  return state;
};

export default userReducer;