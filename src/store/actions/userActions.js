export const createUser = (user) => {
    return (dispatch, getState, { getFirebase, getFirestore }) => {
        const firebase = getFirebase();
        const firestore = getFirestore();
        if (user.email && user.password && (user.password == user.passwordRepeat)) {
            firebase.auth().createUserWithEmailAndPassword(user.email, user.password).then(() => {
                firestore.collection('users').add({...user}).then(() => {
                    dispatch({ type: 'CREATE_USER_SUCCESS' });
                }).catch(err => {
                    console.log(err);
                    dispatch({ type: 'CREATE_USER_ERROR' }, err);
                });
            }).catch((err) => {
                console.log(err);
            });
        }
    }
};