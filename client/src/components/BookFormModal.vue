<template>
  <div
    v-if="visible"
    class="fixed inset-0 z-50 flex items-center justify-center bg-black/50 backdrop-blur-sm"
  >
    <div class="bg-white w-full max-w-lg rounded-2xl shadow-2xl p-8 relative">
      <h2 class="text-2xl font-bold text-gray-800 mb-6 text-center">
        {{ isEditMode ? "Update Book" : "Add New Book" }}
      </h2>

      <form @submit.prevent="handleSubmit" class="space-y-4">
        <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
          <div>
            <label class="block text-sm font-medium text-gray-700 mb-1"
              >ISBN</label
            >
            <input
              type="number"
              v-model="form.isbn"
              class="w-full border border-gray-300 rounded-lg px-4 py-2 focus:ring-2 focus:ring-blue-500 focus:outline-none"
              required
            />
          </div>
          <div>
            <label class="block text-sm font-medium text-gray-700 mb-1"
              >Title</label
            >
            <input
              type="text"
              v-model="form.title"
              class="w-full border border-gray-300 rounded-lg px-4 py-2 focus:ring-2 focus:ring-blue-500 focus:outline-none"
              required
            />
          </div>
          <div>
            <label class="block text-sm font-medium text-gray-700 mb-1"
              >Author</label
            >
            <input
              type="text"
              v-model="form.author"
              class="w-full border border-gray-300 rounded-lg px-4 py-2 focus:ring-2 focus:ring-blue-500 focus:outline-none"
              required
            />
          </div>
          <div>
            <label class="block text-sm font-medium text-gray-700 mb-1"
              >Available Copies</label
            >
            <input
              type="number"
              v-model.number="form.available_copies"
              class="w-full border border-gray-300 rounded-lg px-4 py-2 focus:ring-2 focus:ring-blue-500 focus:outline-none"
              required
            />
          </div>
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
            {{ isEditMode ? "Update Book" : "Add Book" }}
          </button>
        </div>
      </form>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import { toast } from "vue3-toastify";

export default {
  name: "BookFormModal",
  props: {
    visible: Boolean,
    book: Object,
  },
  data() {
    return {
      form: {
        isbn: "",
        title: "",
        author: "",
        available_copies: 0,
      },
    };
  },
  computed: {
    isEditMode() {
      return !!this.book;
    },
  },
  watch: {
    book: {
      immediate: true,
      handler(newVal) {
        if (newVal) {
          this.form = { ...newVal };
        } else {
          this.resetForm();
        }
      },
    },
  },
  methods: {
    async handleSubmit() {
      try {
        if (this.isEditMode) {
          await axios.put(
            `http://localhost:8000/api/books/${this.book.id}/`,
            this.form
          );
        } else {
          await axios.post("http://localhost:8000/api/books/", this.form);
        }
        this.$emit("saved");
        this.close();
        toast.success("Saved successfully!", {
          autoClose: 1500,
          pauseOnFocusLoss: false,
        });
      } catch (error) {
        const message =
          error.response?.data?.isbn?.[0] || "Something went wrong.";
        toast.error(message, {
          autoClose: 2000,
          pauseOnFocusLoss: false,
        });
      }
    },
    resetForm() {
      this.form = {
        isbn: "",
        title: "",
        author: "",
        available_copies: 0,
      };
    },
    close() {
      this.$emit("close");
      this.resetForm();
    },
  },
};
</script>
