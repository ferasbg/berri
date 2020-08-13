const initState = {};

const userReducer = (state = initState, action) => {
  switch (action.type) {
    case 'CREATE_USER_SUCCESS':
      console.log('create user', action.user);
      return state;
    default:
      return state;
  }
};

export default userReducer;