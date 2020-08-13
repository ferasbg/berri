export const signUp = (credentials) => {
    return (dispatch, getState, { getFirebase, getFirestore }) => {
        const firebase = getFirebase();
        const firestore = getFirestore();
        
        if (credentials.email && credentials.password && (credentials.password == credentials.passwordRepeat)) {
            firebase.auth().createUserWithEmailAndPassword(
                credentials.email,
                credentials.password
            ).then((resp) => {
                return firestore.collection('users').doc(credentials.email).set({
                    email: credentials.email,
                    first: credentials.first,
                    last: credentials.last,
                    usertype: 'Student',
                    prof_pic: 'https://i.ibb.co/HtsTkv5/profile-pic.png'
                });
            }).then(() => {
                dispatch({ type: 'SIGNUP_SUCCESS' });
            }).catch((err) => {
                dispatch({ type: 'SIGNUP_ERROR', err });
            });
        } else {
            dispatch({ type: 'VERIF_ERROR' });
        }
    }
}

export const signIn = (credentials) => {
    return (dispatch, getState, {getFirebase}) => {
        const firebase = getFirebase();
        
        firebase.auth().signInWithEmailAndPassword(
            credentials.email,
            credentials.password
        ).then(() => {
            dispatch({ type: 'LOGIN_SUCCESS' });
        }).catch((err) => {
            dispatch({ type: 'LOGIN_ERROR', err });
        });
    }
}

export const gSignIn = (user, token) => {
    console.log(token);
    return (dispatch, getState, { getFirebase, getFirestore }) => {
        const firebase = getFirebase();
        const firestore = getFirestore();
        let email = user.email;
        let name = user.name;
        let picUrl =  user.imageUrl;
        let first = name.split(" ")[0];
        let last = name.split(" ")[1];
        let docRef = firestore.collection('users').doc(email);
        docRef.get().then(doc => {
            if (!doc.exists) {
                return docRef.set({
                    email,
                    first,
                    last,
                    usertype: 'Student',
                    prof_pic: picUrl,
                });
            } else return;
        })
        .then(() => {
            dispatch({ type: 'LOGIN_SUCCESS' });
        }).catch((err) => {
            dispatch({ type: 'LOGIN_ERROR', err });
        });
    }
}

export const signOut = () => {
    return (dispatch, getState, {getFirebase}) => {
        const firebase = getFirebase();

        firebase.auth().signOut().then(() => {
            dispatch({ type: 'SIGNOUT_SUCCESS' })
        });
    }
}