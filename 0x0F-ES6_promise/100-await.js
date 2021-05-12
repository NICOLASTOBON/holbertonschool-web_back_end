import { uploadPhoto, createUser } from './utils';

async function asyncUploadUser() {
  const photoData = await uploadPhoto();
  const userData = await createUser();

  return { photo: photoData, user: userData };
}

export default asyncUploadUser;
