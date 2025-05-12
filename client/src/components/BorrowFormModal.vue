<template>
  <div
    v-if="visible"
    class="fixed inset-0 z-50 flex items-center justify-center bg-black/50 backdrop-blur-sm"
  >
    <div class="bg-white w-full max-w-xl rounded-2xl shadow-2xl p-8 relative">
      <h2 class="text-2xl font-bold text-gray-800 mb-6 text-center">
        Borrow Book
      </h2>

      <form @submit.prevent="handleSubmit" class="space-y-5">
        <div>
          <label class="block text-sm font-medium text-gray-700 mb-1"
            >User</label
          >
          <select
            v-model="form.user"
            class="w-full border border-gray-300 rounded-lg px-4 py-2 focus:ring-2 focus:ring-blue-500 focus:outline-none"
            required
          >
            <option disabled value="">Select a user</option>
            <option v-for="user in users" :key="user.id" :value="user.id">
              {{ user.first_name }} {{ user.last_name }}
            </option>
          </select>
        </div>

        <div>
          <label class="block text-sm font-medium text-gray-700 mb-1"
            >Book</label
          >
          <select
            v-model="form.book"
            class="w-full border border-gray-300 rounded-lg px-4 py-2 focus:ring-2 focus:ring-blue-500 focus:outline-none"
            required
          >
            <option disabled value="">Select a book</option>
            <option v-for="book in books" :key="book.id" :value="book.id">
              {{ book.title }}
            </option>
          </select>
        </div>

        <div>
          <label class="block text-sm font-medium text-gray-700 mb-1"
            >Date</label
          >
          <input
            type="date"
            v-model="form.date"
            class="w-full border border-gray-300 rounded-lg px-4 py-2 focus:ring-2 focus:ring-blue-500 focus:outline-none"
            required
          />
        </div>

        <div class="flex justify-end gap-3 pt-4">
          <button
            type="button"
            @click="close"
            class="px-4 py-2 rounded-lg border border-gray-300 text-gray-700 hover:bg-gray-100 transition"
          >
            Cancel
          </button>
          <button
            type="submit"
            class="px-5 py-2 rounded-lg bg-blue-600 text-white hover:bg-blue-700 transition"
          >
            Submit
          </button>
        </div>
      </form>
    </div>
  </div>
</template>

<script setup>
import { reactive, watch, ref } from "vue";
import axios from "axios";
import { toast } from "vue3-toastify";

const props = defineProps({
  visible: Boolean,
});

const emit = defineEmits(["close", "saved"]);

const form = reactive({
  book: "",
  user: "",
  status: "borrowed",
  date: new Date().toISOString().split("T")[0],
});

const books = ref([]);
const users = ref([]);

watch(
  () => props.visible,
  async (newVal) => {
    if (newVal) {
      await fetchBooksAndUsers();
    }
  },
  { immediate: true }
);

async function fetchBooksAndUsers() {
  try {
    const [booksResponse, usersResponse] = await Promise.all([
      axios.get("http://localhost:8000/api/books/"),
      axios.get("http://localhost:8000/api/users/"),
    ]);

    books.value = booksResponse.data;
    users.value = usersResponse.data;
  } catch (error) {
    console.error("Failed to fetch books or users:", error);
  }
}

function resetForm() {
  form.book = "";
  form.user = "";
  form.date = new Date().toISOString().split("T")[0];
}

async function handleSubmit() {
  try {
    await axios.post("http://localhost:8000/api/borrow/", form);
    emit("saved");
    close();
    toast.success("Book borrowed successfully!", {
      autoClose: 1500,
      pauseOnFocusLoss: false,
    });
  } catch (error) {
    const errorResponse = error.response?.data;
    toast.error(errorResponse?.error || "Something went wrong.", {
      autoClose: 1500,
      pauseOnFocusLoss: false,
    });
  }
}

function close() {
  resetForm();
  emit("close");
}
</script>
