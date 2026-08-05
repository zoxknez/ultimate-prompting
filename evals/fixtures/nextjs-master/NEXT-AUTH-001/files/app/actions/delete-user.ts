"use server";

import { db } from "@/lib/db";

// Vulnerable: this Server Action deletes any user by id with no check that
// the caller is that user or an admin. Any authenticated session - or,
// depending on how this action is wired to the client, any caller who can
// reach it at all - can delete an arbitrary account by passing its id.
export async function deleteUser(userId: string) {
  console.log(`Deleting user ${userId}`);
  await db.user.delete({ where: { id: userId } });
  return { success: true };
}
